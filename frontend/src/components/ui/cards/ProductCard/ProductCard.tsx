import React from "react";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import CardMedia from "@mui/material/CardMedia";
import { CardActionArea } from "@mui/material";
export default function ProductCard({ product }: any) {
  return (
    <Card
      variant="outlined"
      sx={{ maxWidth: 300, width: "100%", flex: "1 0 20%" }}
    >
      <CardActionArea href={`/products/${product.slug}`}>
        <CardMedia
          sx={{ height: 200 }}
          image="https://mui.com/static/images/cards/contemplative-reptile.jpg"
          title="green iguana"
        />
        <CardContent>
          <Typography variant="h5" component="div">
            {product.product_name}
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            {product.blurb}
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
