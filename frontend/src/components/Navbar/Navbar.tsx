import { MegaMenu } from "primereact/megamenu";
import logo from "../../assets/hat_chief.svg";
import "./Navbar.styles.css";

export default function Navbar() {
  const items = [
    {
      label: "Recipe of the day",
      url: "/",
    },
    {
      label: "History",
      url: "/history",
    },
    {
      label: "About",
      url: "/about",
    },
  ];

  const start = <img alt="logo" src={logo} height="40" className="p-mr-2" />;

  return (
    <div className="custom-navbar">
      <div className="navbar-items">
        <MegaMenu
          model={items}
          orientation="horizontal"
          start={start}
          breakpoint="500px"
          style={{ backgroundColor: "transparent" }}
        />
      </div>
    </div>
  );
}
