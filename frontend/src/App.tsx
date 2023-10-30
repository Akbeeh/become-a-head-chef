import { PrimeReactProvider } from "primereact/api";
import { Route, Routes } from "react-router-dom";
import "./App.css";
import About from "./pages/About.tsx";
import History from "./pages/History.tsx";
import Home from "./pages/Home.tsx";

function App() {
  return (
    <PrimeReactProvider>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/history" element={<History />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </PrimeReactProvider>
  );
}

export default App;
