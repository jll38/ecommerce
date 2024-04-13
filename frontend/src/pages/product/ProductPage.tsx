import React from "react";
import { useParams } from "react-router-dom";

import { getProductInfo } from "../../services/Product";

import AddToCart from "../../components/ui/buttons/AddToCart/AddToCart";
import RadioProduct from "../../components/ui/buttons/RadioProduct/RadioProduct";

export default function ProductPage() {
  const { productID } = useParams();
  const [productInfo, setProductInfo] = React.useState<any>();
  const [loading, setLoading] = React.useState<boolean>(true);
  
  React.useEffect(() => {
    const fetchProduct = async () => {
      console.log(productID);
      if (productID) {
        const product = await getProductInfo(productID);
        console.log(product);
        setProductInfo(product);
        setLoading(false);
      }
    };

    fetchProduct();
  }, [productID]);

  return (
    <main>
      <section id="product-info" className="flex gap-[3rem] justify-evenly">
        {loading ? (
          <div>Loading</div>
        ) : (
          <>
            <aside className="w-full max-w-[600px] h-[600px]">img here</aside>
            <section
              id="purchase-info"
              className="w-full max-w-[400px] h-[600px] pt-2 px-0 flex flex-col gap-4"
            >
              <div className="flex flex-col gap-2">
                <h2 className="text-2xl font-semibold">{productInfo.product_name}</h2>
                <h3 className="text-xl">${productInfo.price}</h3>
                <p className="text-sm text-black/70">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </p>
              </div>
              <hr></hr>
              <div className="flex flex-col gap-2">
                <h4 className="text-sm text-black/70">Color:</h4>
                <RadioProduct value={["Red", "Black", "Green", "White"]}/>
              </div>
              <hr></hr>
              <div className="flex flex-col gap-2">
                <h4 className="text-sm text-black/70">Size:</h4>
                <RadioProduct value={["SM", "MD", "LG", "XL"]}/>
              </div>
              <hr></hr>
              <div className="flex flex-col gap-2">
                <AddToCart route={productInfo["_links"].add_to_cart} />
              </div>
              <hr></hr>
              <div className="flex flex-col gap-2">
                <h4 className="text-md">Description</h4>
                <p className="text-sm text-black/70">
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                  irure dolor in reprehenderit in voluptate velit esse cillum
                  dolore eu fugiat nulla pariatur. Excepteur sint occaecat
                  cupidatat non proident, sunt in culpa qui officia deserunt
                  mollit anim id est laborum.
                </p>
              </div>
            </section>
          </>
        )}
      </section>
    </main>
  );
}
