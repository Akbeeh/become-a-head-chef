import { Footer, Navbar } from "../components/index.tsx";

function About() {
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
        <div className="content-container">
          <p
            className="flex justify-content-center text-center"
            style={{ fontSize: "1.25rem" }}
          >
            Our mission is simple: to bring excitement and innovation to your
            daily meals. With our unique concept, you can kiss routine goodbye
            and say hello to a new culinary journey each day of the week.
          </p>
          <div className="card">
            <ul>
              <li>
                <span>
                  <strong>Monday Dessert</strong>: Start your week with a
                  delightful dessert.
                </span>
              </li>
              <li>
                <span>
                  <strong>Tuesday Breakfast & Brunch</strong>: Enjoy a morning
                  treat to kickstart your day.
                </span>
              </li>
              <li>
                <span>
                  <strong>Wednesday Lunch</strong>: Explore new lunch ideas
                  midweek.
                </span>
              </li>
              <li>
                <span>
                  <strong>Thursday Healthy</strong>: Discover nutritious and
                  wholesome recipes to boost your well-being.
                </span>
              </li>
              <li>
                <span>
                  <strong>Friday Appetizers & Snacks</strong>: Get ready for the
                  weekend with tasty finger foods.
                </span>
              </li>
              <li>
                <span>
                  <strong>Saturday Salads</strong>: Savor refreshing salads for
                  a healthy weekend.
                </span>
              </li>
              <li>
                <span>
                  <strong>Sunday Drinks</strong>: Unwind with a selection of
                  beverages to complete your weekend.
                </span>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}

export default About;
