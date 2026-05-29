// A reusable skill input that lets users add and remove skill tags

import { useState } from 'react';

function SkillInput({ skills, setSkills }) {
  const [inputValue, setInputValue] = useState('');

  // Add a skill to the list when user presses Enter or clicks Add
  const addSkill = () => {
    const trimmed = inputValue.trim();

    // Don't add empty or duplicate skills
    if (!trimmed || skills.includes(trimmed)) {
      setInputValue('');
      return;
    }

    setSkills([...skills, trimmed]); // Add to the array
    setInputValue('');
  };

  // Remove a skill when user clicks the × button
  const removeSkill = (skillToRemove) => {
    setSkills(skills.filter(s => s !== skillToRemove));
  };

  // Allow pressing Enter to add a skill
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      addSkill();
    }
  };

  return (
    <div className="form-group">
      <label>Skills you already know</label>

      {/* Display existing skills as removable tags */}
      <div className="skill-tags">
        {skills.map(skill => (
          <span key={skill} className="skill-tag">
            {skill}
            <button
              type="button"
              onClick={() => removeSkill(skill)}
              className="remove-tag"
              aria-label={`Remove ${skill}`}
            >
              ×
            </button>
          </span>
        ))}
      </div>

      {/* Input to add new skills */}
      <div className="skill-input-row">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="e.g. Python, HTML, SQL"
        />
        <button type="button" onClick={addSkill} className="add-btn">
          Add
        </button>
      </div>
    </div>
  );
}

export default SkillInput;
