import { PrimeReactProvider } from "primereact/api";
import { Route, Routes } from "react-router-dom";
import "./App.css";
import History from "./pages/History.tsx";
import Home from "./pages/Home.tsx";

function App() {
  return (
    <PrimeReactProvider>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </PrimeReactProvider>
  );
}

export default App;
