jQuery(function ($) {

document.getElementById('products_count').addEventListener('input', function(){
  var products = parseInt(this.value);
  var product_items = document.getElementById('product_items');
  product_items.innerHTML = '';

  for (var i = 1; i <= products; i++){
      var div = document.createElement('div');
      div.innerHTML = `

      <hr/>
      <h5 class="text-center"> Item section ${i} </h5>

      <div class="d-flex">

          <div class="col container-fluid">
              <div class="mb-3">
                  <label for="product_name" class="form-label">Product Name</label>
                  <input type="text" name="product_name_${i}" id="product_name_${i}" class="form-control" placeholder="Enter the name of product" Required/>
                  <small class="text-muted">Cannot be empty</small>
              </div>
          </div>
          <div class="col container-fluid">
              <div class="mb-3">
                  <label for ="product_code" class="form-label">Product Code</label>
                  <select name="product_code_${i}" id="product_code_${i}" class="form-control text-center" placeholder="Enter Product Code" Required>
                      <option value="">Select Vendo Code</option>
                      <option value="A01">A01</option>
                      <option value="A02">A02</option>
                      <option value="A03">A03</option>
                      <option value="A04">A04</option>
                      <option value="B05">B05</option>
                      <option value="B06">B06</option>
                      <option value="B07">B07</option>
                      <option value="B08">B08</option>
                      <option value="C09">C09</option>
                      <option value="C10">C10</option>
                      <option value="C11">C11</option>
                      <option value="C12">C12</option>
                      <option value="D13">D13</option>
                      <option value="D14">D14</option>
                      <option value="D15">D15</option>
                      <option value="D16">D16</option>
                  </select>
                  <small class="text-muted">Input a unique code for a product item</small>
              </div>
          </div>
          <div class="col container-fluid">
              <div class="mb-3">
                  <label for="product_price" class="form-label">Price</label>
                  <input type="text" name="product_price_${i}" id="product_price_${i}" class="form-control" placeholder="Input Price in Php" Required/>
                  <small class="text-muted">Equivalent to BCH: </small>
              </div>
          </div>
          <div class="col container-fluid">
              <div class="mb-3">
                  <label for="product_quantity" class="form-label">Product Quantity</label>
                  <input type="text" name="product_quantity_${i}" id="product_quantity_${i}" class="form-control" placeholder="Enter Product Quantity" Required/>
                  <small class="text-muted">Product Quantity may vary depending on the <b>Product Code</b></small>
              </div>
          </div>

      </div>

      <div class="d-flex">
          <div class="col container-fluid">
              <div class="lg-6">
                  <label for="product_image" class="form-label">Product Image</label>
                  <input type="file" name="product_image_${i}" id="product_image_${i}" class="form-control" placeholder="Choose product image" accept="image/png, image/jpeg" Required/>
                  <small class="text-muted">Image file supported: JPEG/PNG</small>
              </div>
          </div>
          <div class="col container-fluid">
              <div class="lg-3" style="margin-top: -13px">
                  <br>
                  <br>
                      <button type="button" class="lg-3 btn btn-danger" onclick="deselectImage('product_image_${i}')">Deselect Image</button>
              </div>
          </div>
      </div>
      `;
      product_items.appendChild(div);
  }
})

});

function deselectImage(inputId){
    var input = document.getElementById(inputId);
    input.value = ''; // Clear the input value
  }