// Displays a single generated roadmap with phases and topics

function RoadmapCard({ roadmap, onMarkTopic }) {
  // Build a lookup of which topics are marked complete
  // { "HTML5": true, "CSS3": false, ... }
  const completedTopics = {};
  if (roadmap.progress) {
    roadmap.progress.forEach(p => {
      completedTopics[p.topic_name] = p.is_completed;
    });
  }

  return (
    <div className="roadmap-card">
      {/* Card header */}
      <div className="roadmap-header">
        <h3 className="roadmap-goal">{roadmap.career_goal}</h3>
        <span className="roadmap-date">
          {new Date(roadmap.created_at).toLocaleDateString()}
        </span>
      </div>

      {/* Input skills shown as small badges */}
      <p className="roadmap-skills">
        <strong>Your skills:</strong> {roadmap.skills_input || 'None specified'}
      </p>

      {/* Render each phase */}
      {roadmap.phases && roadmap.phases.map((phase) => (
        <div key={phase.phase} className={`phase-block phase-${phase.phase}`}>
          <div className="phase-header">
            <span className="phase-num">Phase {phase.phase}</span>
            <span className="phase-title">{phase.title}</span>
            <span className="phase-duration">{phase.duration}</span>
          </div>

          {/* List of topics as checkboxes */}
          <ul className="topic-list">
            {phase.topics.map((topic) => {
              const isDone = completedTopics[topic] || false;
              return (
                <li key={topic} className={`topic-item ${isDone ? 'done' : ''}`}>
                  {/* Clicking the checkbox calls the parent handler */}
                  <input
                    type="checkbox"
                    checked={isDone}
                    onChange={() => onMarkTopic(roadmap.id, topic, isDone)}
                    id={`${roadmap.id}-${topic}`}
                  />
                  <label htmlFor={`${roadmap.id}-${topic}`}>{topic}</label>
                </li>
              );
            })}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default RoadmapCard;
