import { useEffect, useState } from "react";
import RunnersList from "./components/RunnersList";

function App() {
  const [runners, setRunners] = useState([]);

  useEffect(() => {
    fetchRunners();
  }, []);

  const fetchRunners = async () => {
    const response = await fetch("http://127.0.0.1:5000/runners");
    const data = await response.json();
    setRunners(data.runners);
    console.log(data.runners);
  };
  return (
    <>
      <RunnersList runners={runners} />
    </>
  );
}

export default App;
