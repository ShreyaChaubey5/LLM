import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
import { QueryProvider } from "./context/QueryContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <QueryProvider>
    <App />
  </QueryProvider>
);

