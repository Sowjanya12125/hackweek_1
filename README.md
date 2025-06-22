<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>front-end</title>
  <style>
    .star-rating {
      direction: rtl;
      font-size: 2rem;
      unicode-bidi: bidi-override;
      text-align: center;
    }

    .star-rating input {
      display: none;
    }

    .star-rating label {
      color: lightgray;
      cursor: pointer;
    }

    .star-rating input:checked ~ label,
    .star-rating label:hover,
    .star-rating label:hover ~ label {
      color: gold;
    }
  </style>
</head>
<body style="background-color: white;">
    <img src="c:\Users\shiva\Desktop\hackweek.jpeg" alt=" " height="110px" width="150px">
    <h1 style="color: black;"><b>Skytech Gaming PC Desktop – Intel Core i7 12700F 2.1 GHz, NVIDIA RTX 4070 Ti, 1TB NVME SSD, 16GB DDR4 RAM 3200, 750W Gold PSU, 360mm AIO, 11AC Wi-Fi, Windows 11 Home 64-bit,Black</b></h1>

  <div class="star-rating">
    <input type="radio" id="star5" name="rating" value="5"><label for="star5">&#9733;</label>
    <input type="radio" id="star4" name="rating" value="4"><label for="star4">&#9733;</label>
    <input type="radio" id="star3" name="rating" value="3"><label for="star3">&#9733;</label>
    <input type="radio" id="star2" name="rating" value="2"><label for="star2">&#9733;</label>
    <input type="radio" id="star1" name="rating" value="1"><label for="star1">&#9733;</label>
  </div>
  <h5><b>50+ bought in past month</b></h5>
  <h3>$1,979.59</h3>
  <button type="submit" style="background-color: yellow;">add to cart</button>
  <button type="submit" style="background-color: yellow;">buy now :)</button>
</body>
</html>
