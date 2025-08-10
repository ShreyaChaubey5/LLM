import React from "react";
import { uploadDocument } from "./services/api";

function UploadPage() {
  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (file) {
      try {
        const result = await uploadDocument(file);
        console.log("Uploaded:", result);
      } catch (err) {
        console.error(err);
      }
    }
  };

  return (
    <div>
      <h1>Upload Document</h1>
      <input type="file" onChange={handleFileChange} />
    </div>
  );
}

export default UploadPage;
