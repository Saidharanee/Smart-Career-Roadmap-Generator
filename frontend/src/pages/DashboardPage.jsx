import { useState, useEffect } from 'react';
import { generateRoadmap, getRoadmaps, markTopic } from '../api/api';
import RoadmapCard from '../components/RoadmapCard';
import SkillInput from '../components/SkillInput';

const CAREER_GOALS = [
  'Full Stack Developer', 
  'Backend Developer', 
  'Data Analyst',
  'Frontend Developer',
  'AI/ML Engineer',
  'DevOps Engineer',
  'Software Developer',
  'Data Engineer',
  'Python Developer',
  'App Developer',
];

function DashboardPage({ onLogout }) {
  const username = localStorage.getItem('username');
  const [careerGoal, setCareerGoal] = useState(CAREER_GOALS[0]);
  const [skills, setSkills] = useState([]);
  const [roadmaps, setRoadmaps] = useState([]);
  const [newRoadmap, setNewRoadmap] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => { loadRoadmaps(); }, []);

  const loadRoadmaps = async () => {
    try {
      const res = await getRoadmaps();
      setRoadmaps(res.data);
    } catch {
      console.error('Could not load roadmaps');
    }
  };

  const handleGenerate = async () => {
    if (skills.length === 0) { setError('Please add at least one skill.'); return; }
    setError('');
    setLoading(true);
    try {
      const res = await generateRoadmap(careerGoal, skills);
      setNewRoadmap(res.data);
      loadRoadmaps();
    } catch {
      setError('Failed to generate. Make sure Django backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleMarkTopic = async (roadmapId, topicName, currentStatus) => {
    await markTopic(roadmapId, topicName, !currentStatus);
    loadRoadmaps();
    if (newRoadmap && newRoadmap.id === roadmapId) {
      const res = await getRoadmaps();
      const updated = res.data.find(r => r.id === roadmapId);
      if (updated) setNewRoadmap(updated);
    }
  };

  return (
    <div>
      <nav className="navbar">
        <span className="nav-logo">🗺 Career Roadmap</span>
        <div className="nav-right">
          <span className="nav-user">Hi, {username}!</span>
          <button className="logout-btn" onClick={onLogout}>Logout</button>
        </div>
      </nav>

      <div className="dashboard-body">
        <div className="input-panel">
          <h2>🗺 Build My Roadmap</h2>
          <div className="form-group">
            <label>Career Goal</label>
            <select value={careerGoal} onChange={e => setCareerGoal(e.target.value)}>
              {CAREER_GOALS.map(g => <option key={g} value={g}>{g}</option>)}
            </select>
          </div>

          <SkillInput skills={skills} setSkills={setSkills} />

          {error && <p className="error-msg">{error}</p>}

          <button className="generate-btn" onClick={handleGenerate} disabled={loading}>
            {loading ? 'Generating…' : '✨ Generate Roadmap'}
          </button>
        </div>

        <div className="roadmap-panel">
          {newRoadmap && (
            <div>
              <h3 className="panel-heading">✅ Your New Roadmap</h3>
              <RoadmapCard roadmap={newRoadmap} onMarkTopic={handleMarkTopic} />
            </div>
          )}

          {roadmaps.length > 0 && (
            <div>
              <h3 className="panel-heading">📂 Saved Roadmaps</h3>
              {roadmaps.map(rm => (
                <RoadmapCard key={rm.id} roadmap={rm} onMarkTopic={handleMarkTopic} />
              ))}
            </div>
          )}

          {roadmaps.length === 0 && !newRoadmap && (
            <div className="empty-state">
              <p>No roadmaps yet. Fill in the form and click Generate! 👈</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default DashboardPage;
