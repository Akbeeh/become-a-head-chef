import { CustomDataView, Footer, Navbar } from "../components/index.tsx";

function History() {
  return (
    <>
      <Navbar />
      <div>
        <div className="head-container">
          <h1>Become a Head Chef</h1>
          <p>
            Master the culinary arts by exploring and preparing a new dish every
            day!
          </p>
        </div>
        <CustomDataView />
      </div>
      <Footer />
    </>
  );
}

export default History;
