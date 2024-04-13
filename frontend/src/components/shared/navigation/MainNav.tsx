import React from "react";

export default function MainNav() {
  const navLinks = [
    {
      label: "New Arrivals",
      href: "/new-arrivals",
    },
    {
      label: "Tops",
      href: "/tops",
    },
    {
      label: "Bottoms",
      href: "/bottoms",
    },
    {
      label: "Shoes",
      href: "/shoes",
    },
    {
      label: "Sale",
      href: "/sale",
    },
  ];
  return (
    <nav id="main-nav">
      <ul>
        {navLinks.map((link) => (
          <li key={link.label}>{link.label}</li>
        ))}
      </ul>
    </nav>
  );
}
