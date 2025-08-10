// Send file + query in one request
export async function submitQuery(file, query) {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("query", query);

  const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/query`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    throw new Error(`Query failed: ${response.status}`);
  }

  return await response.json();
}

// Optional: for separate file upload API
export async function uploadDocument(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/upload/document`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    throw new Error(`Upload failed: ${response.status}`);
  }

  return await response.json();
}
