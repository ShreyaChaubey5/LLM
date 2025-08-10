import React, { createContext, useContext, useState } from "react";

// Create the context
const QueryContext = createContext();

// Provider component
export const QueryProvider = ({ children }) => {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  return (
    <QueryContext.Provider
      value={{
        file,
        setFile,
        query,
        setQuery,
        result,
        setResult,
      }}
    >
      {children}
    </QueryContext.Provider>
  );
};

// Custom hook for easy access
export const useQueryContext = () => {
  return useContext(QueryContext);
};
