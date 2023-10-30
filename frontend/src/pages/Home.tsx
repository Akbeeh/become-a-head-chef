import { Footer, Navbar, Recipe } from "../components/index.tsx";

function Home() {
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
        <Recipe />
      </div>
      <Footer />
    </>
  );
}

export default Home;
