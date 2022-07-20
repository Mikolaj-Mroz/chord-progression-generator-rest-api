import './App.css';
import React, { useEffect, useState } from 'react';

function App() {
  const [progression, setProgression] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/").then((res) =>
        res.json().then((data) => {
          setProgression(data.progression)
        })
    );
  }, []);

  console.log(progression)

  return <div className="App"/>;
}

export default App;
