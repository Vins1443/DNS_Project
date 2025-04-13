import React, { useEffect, useState } from "react";

function App() {
  const [text, setText] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/file")
      .then(res => res.text())
      .then(data => setText(data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Labour Act - Structured Text</h1>
      <pre style={{ whiteSpace: "pre-wrap", fontFamily: "monospace" }}>{text}</pre>
    </div>
  );
}

export default App;
