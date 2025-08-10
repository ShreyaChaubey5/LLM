import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <img src="/logo.svg" alt="Logo" width="30" height="30" />
        Clause Retriever
      </div>
      <div>
        <Link to="/">Home</Link>
        <Link to="/results">Results</Link>
      </div>
    </nav>
  );
};

export default Navbar;
