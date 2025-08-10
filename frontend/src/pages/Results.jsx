import React from "react";
import Navbar from "../components/Navbar";
import ResultCard from "../components/ResultCard";
import { useQueryContext } from "../context/QueryContext";
import { useNavigate } from "react-router-dom";

const Results = () => {
  const { result } = useQueryContext();
  const navigate = useNavigate();

  if (!result) {
    // If no result in context, redirect back to home
    navigate("/");
    return null;
  }

  const handleDownload = () => {
    const blob = new Blob([JSON.stringify(result, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "decision_result.json";
    a.click();
  };

  return (
    <div>
      <Navbar />
      <div className="max-w-3xl mx-auto mt-10 px-4">
        <ResultCard
          decision={result.decision}
          clauses={result.clauses}
          justification={result.justification}
          onDownload={handleDownload}
        />
      </div>
    </div>
  );
};

export default Results;
