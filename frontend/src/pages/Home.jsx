// import React, { useState } from "react";
// import Navbar from "../components/Navbar";
// import FileUpload from "../components/FileUpload";
// import QueryInput from "../components/QueryInput";
// import Loader from "../components/Loader";
// import { useNavigate } from "react-router-dom";
// import { useQueryContext } from "../context/QueryContext";
// import { submitQuery } from "../services/api";

// const Home = () => {
//   const { file, setFile, setQuery, setResult } = useQueryContext();
//   const [isLoading, setIsLoading] = useState(false);
//   const navigate = useNavigate();

//   const handleQuerySubmit = async (queryText) => {
//     if (!file) {
//       alert("Please upload a document first!");
//       return;
//     }

//     setQuery(queryText);
//     setIsLoading(true);

//     try {
//       // Call the backend API
//       const response = await submitQuery(file, queryText);

//       // Save the result from API into context
//       setResult(response);

//       // Navigate to results page
//       navigate("/results");
//     } catch (error) {
//       console.error("Error submitting query:", error);
//       alert("Something went wrong while processing your query.");
//     } finally {
//       setIsLoading(false);
//     }
//   };

//   return (
//     <div>
//       <Navbar />
//       <div className="container">
//         <FileUpload onFileSelect={setFile} />
//         {file && (
//           <p>Selected File: {file.name}</p>
//         )}
//         {isLoading ? (
//           <Loader />
//         ) : (
//           <QueryInput onSubmit={handleQuerySubmit} isLoading={isLoading} />
//         )}
//       </div>
//     </div>
//   );
// };

// export default Home;
import React, { useState } from "react";
import Navbar from "../components/Navbar";
import FileUpload from "../components/FileUpload";
import QueryInput from "../components/QueryInput";
import Loader from "../components/Loader";
import { useNavigate } from "react-router-dom";
import { useQueryContext } from "../context/QueryContext";
import { submitQuery } from "../services/api";

const Home = () => {
  const { file, setFile, setQuery, setResult } = useQueryContext();
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleQuerySubmit = async (queryText) => {
    if (!file) {
      alert("Please upload a document first!");
      return;
    }

    setQuery(queryText);
    setIsLoading(true);

    try {
      // Send file + query to backend
      const response = await submitQuery(file, queryText);
      setResult(response);
      navigate("/results");
    } catch (error) {
      console.error("Error submitting query:", error);
      alert("Something went wrong while processing your query.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <Navbar />
      <div className="container">
        <FileUpload onFileSelect={setFile} />
        {file && <p>Selected File: {file.name}</p>}
        {isLoading ? (
          <Loader />
        ) : (
          <QueryInput onSubmit={handleQuerySubmit} isLoading={isLoading} />
        )}
      </div>
    </div>
  );
};

export default Home;
