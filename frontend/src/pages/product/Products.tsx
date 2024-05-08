import React from "react";

//Methods
import { getProductList } from "../../services/Product";

//Components
import ProductCard from "../../components/ui/cards/ProductCard/ProductCard";
import { Typography } from "@mui/material";
import { Button } from "@mui/material";
export default function Products() {
  const [products, setProducts] = React.useState<any>();
  const [loading, setLoading] = React.useState<boolean>(true);

  React.useEffect(() => {
    const fetchProducts = async () => {
      const response = await getProductList({ page: 0, limit: 10 });
      setProducts(response);
      setLoading(false);
    };

    fetchProducts();
  }, []);
  return (
    <main>
      <section id="filters">
        <Button variant="outlined">Fit</Button>
        <Button variant="outlined">Color</Button>
        <Button variant="outlined">Price</Button>
      </section>
      <section
        id="product-info"
        className="flex flex-wrap gap-[3rem] justify-evenly"
      >
        {loading ? (
          <div>Loading...</div>
        ) : (
          <>
            {products ? (
              <>
                {
                  //@ts-ignore
                  products.map((product, i) => (
                    <ProductCard product={product} />
                  ))
                }
              </>
            ) : (
              <div>Error retrieving products...</div>
            )}
          </>
        )}
      </section>
    </main>
  );
}
