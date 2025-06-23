<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>front-end</title>
  <style>
    .card {
      width: 300px;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      margin: 50px auto; /* Centers horizontally */
      text-align: center;
      background-color: white;
    }

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
<body style="background-color:black;">
    <div class="card"  style="width: 18rem;">
  <img src="c:\Users\shiva\Desktop\hackweek.jpeg"  class="card-img-top " height="110px" width="150px">
  
  <div class="card-body">
    <h5 class="card-title">Skytech Gaming PC Desktop – Intel Core i7 12700F 2.1 GHz, NVIDIA RTX 4070 Ti, 1TB NVME SSD, 16GB DDR4 RAM 3200, 750W Gold PSU, 360mm AIO, 11AC Wi-Fi, Windows 11 Home 64-bit,Black</h5>
    <div class="star-rating">
    <input type="radio" id="star5" name="rating" value="5"><label for="star5">&#9733;</label>
    <input type="radio" id="star4" name="rating" value="4"><label for="star4">&#9733;</label>
    <input type="radio" id="star3" name="rating" value="3"><label for="star3">&#9733;</label>
    <input type="radio" id="star2" name="rating" value="2"><label for="star2">&#9733;</label>
    <input type="radio" id="star1" name="rating" value="1"><label for="star1">&#9733;</label>
  </div>
    <p class="card-text"><b>50+ bought in past month</b></p>
     <p class="card-text"><b>$1,979.59</b></p>
     <h6>ships to india</h6>
    
    <a href="#" class="btn btn-primary" style="color: yellow;"> add to cart</a>
  </div>
</div>
</body>
</html>
