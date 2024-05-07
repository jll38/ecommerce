import React from "react";
import { getProductList } from "../../services/Product";
export default function Products() {
  const [products, setProducts] = React.useState<any>();
  const [loading, setLoading] = React.useState<boolean>(true);

  React.useEffect(() => {
    const fetchProducts = async () => {
      const response = await getProductList({page: 0, limit: 10});
      setProducts(response);
      setLoading(false);
    };

    fetchProducts();
  }, []);
  return (
    <main>
      <section id="product-info" className="flex gap-[3rem] justify-evenly">
        {products ? <>
        {//@ts-ignore
        products.map((product, i) => (
            <div>{product.product_name}</div>
        ))}</> : <div>Error retrieving products...</div>
    }
      </section>
    </main>
  );
}
