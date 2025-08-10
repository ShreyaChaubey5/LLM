import React from "react";
import { useDropzone } from "react-dropzone";

const FileUpload = ({ onFileSelect }) => {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      "application/pdf": [".pdf"],
      "application/msword": [".doc", ".docx"],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
      "text/plain": [".txt"],
    },
    multiple: false,
    onDrop: (acceptedFiles) => {
      if (acceptedFiles && acceptedFiles.length > 0) {
        onFileSelect(acceptedFiles[0]);
      }
    },
  });

  return (
    <div
      {...getRootProps()}
      className={`file-upload ${isDragActive ? "active" : ""}`}
    >
      <input {...getInputProps()} />
      {isDragActive ? (
        <p className="file-upload-active-text">Drop the file here...</p>
      ) : (
        <>
          <p>
            Drag & drop a document here, or{" "}
            <span className="highlight">click to select</span>
          </p>
          <p className="file-upload-hint">
            Supported formats: PDF, DOC, DOCX, TXT
          </p>
        </>
      )}
    </div>
  );
};

export default FileUpload;
