import "./Footer.styles.css";

export default function Footer() {
  return (
    <div className="layout-footer">
      <div className="footer-content">
        <span className="footer-text" style={{ marginRight: "5px" }}>
          All the data are retrieved on{" "}
          <a href="https://www.allrecipes.com">allrecipes</a>
        </span>
      </div>
      <div className="footer-content">
        <span className="footer-text" style={{ marginRight: "5px" }}>
          Become a Chief © 2023
        </span>
        <span className="footer-text" style={{ marginRight: "5px" }}>
          |
        </span>
        <span className="footer-text" style={{ marginRight: "5px" }}>
          Made by <a href="https://github.com/Akbeeh">William M</a>
        </span>
      </div>
    </div>
  );
}
