import React, { useState } from "react";

const QueryInput = ({ onSubmit, isLoading }) => {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!query.trim()) return;
     console.log("Submit button clicked, query:", query); 
    onSubmit(query);
  };

  return (
    <form onSubmit={handleSubmit} className="query-input">
      <label>Enter your query</label>
      <textarea
        rows="3"
        placeholder="e.g., 46-year-old male, knee surgery in Pune, 3-month-old insurance policy"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button type="submit" disabled={isLoading}>
        {isLoading ? "Processing..." : "Submit Query"}
      </button>
    </form>
  );
};

export default QueryInput;
