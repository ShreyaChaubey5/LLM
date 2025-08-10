import React from "react";

const ResultCard = ({ decision, clauses, justification, onDownload }) => {
  return (
    <div className="result-card">
      {/* Decision */}
      <div className="decision">
        <span
          className={`decision-text ${
            decision?.toLowerCase() === "approved"
              ? "approved"
              : "rejected"
          }`}
        >
          Decision: {decision || "N/A"}
        </span>
      </div>

      {/* Relevant Clauses */}
      <div className="section">
        <h3>Relevant Clauses:</h3>
        {clauses && clauses.length > 0 ? (
          <ul>
            {clauses.map((clause, idx) => (
              <li key={idx}>{clause}</li>
            ))}
          </ul>
        ) : (
          <p>No clauses found</p>
        )}
      </div>

      {/* Justification */}
      <div className="section">
        <h3>Justification:</h3>
        {justification && justification.length > 0 ? (
          <ul>
            {justification.map((point, idx) => (
              <li key={idx}>{point}</li>
            ))}
          </ul>
        ) : (
          <p>No justification provided</p>
        )}
      </div>

      {/* Download Button */}
      {onDownload && (
        <button onClick={onDownload} className="download-btn">
          Download JSON
        </button>
      )}
    </div>
  );
};

export default ResultCard;
