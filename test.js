document.addEventListener('DOMContentLoaded', () => {
    
    // ฟังก์ชันเพื่ออัปเดตจำนวนสินค้า
    function updateProductAmount(element, isAdding) {
      const amountNumber = element.closest('.cart__amount-content').querySelector('.cart__amount-number');
      let currentValue = parseInt(amountNumber.textContent);
  
      let quantity = parseInt({{product.quanity}});
      console.log (quantity);
  
      if (isAdding == true && currentValue < quantity) {
        currentValue += 1;
      }
      if (isAdding == false && currentValue > 1) {
        currentValue -= 1;
      }
  
      amountNumber.textContent = currentValue; // อัปเดตค่าใน DOM
    }
  
    // จัดการการคลิกปุ่ม minus
    document.querySelectorAll('.bx-minus').forEach(button => {
      button.addEventListener('click', function() {
        updateProductAmount(this, false);
      });
    });
  
    // จัดการการคลิกปุ่ม plus
    document.querySelectorAll('.bx-plus').forEach(button => {
      button.addEventListener('click', function() {
        updateProductAmount(this, true);
      });
    });
  
    // จัดการการคลิกปุ่ม "Add to Cart"
    document.querySelectorAll('.button').forEach(button => {
      button.addEventListener('click', function(e) {
        e.preventDefault(); // ป้องกันการโหลดหน้าใหม่
  
        // รับ product ID จาก data attribute ของปุ่ม
        const productId = this.getAttribute('data-product-id');
  
        // รับจำนวนสินค้าจาก <span>
        // รับค่าจำนวนสินค้าจาก <span>
        const quantityElement = document.querySelector('.cart__amount-number');
        const quantity = quantityElement ? parseInt(quantityElement.textContent.trim()) : 1;
  
        console.log(quantityElement);
        console.log(quantity); // แสดงค่า quantity ใน console
  
        // ส่งคำขอ POST ไปยัง endpoint ของ FastAPI
        fetch(`/add-to-cart?product_id=${productId}&quantity=${quantity}`, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'}
        })
        .then(response => {
          if (!response.ok) {
            return response.json().then(err => { throw err; });
          }
          return response.json();
        })
        .then(data => {
          console.log('Success:', data);
          // แสดงข้อความแจ้งเตือนบนหน้าเว็บ
          const alertElement = document.querySelector('.alert');
          if (alertElement) {
            loadAndUpdateCart();
            alertElement.textContent = "Add Product to cart is Successful.";
            alertElement.style.display = 'block';
  
            setTimeout(() => {
              alertElement.style.display = "none";
            }, 2000);
          }
        })
        .catch(error => {
          console.error('Error:', error);
          // แสดงข้อความแจ้งเตือนข้อผิดพลาด
          const alertElement = document.querySelector('.alert');
          if (alertElement) {
            alertElement.textContent = "Unsuccessful";
            alertElement.style.display = 'block';
          }
        });
      });
    });
  
    // ฟังก์ชันสำหรับโหลดและอัปเดตตะกร้าสินค้า
    function loadAndUpdateCart() {
      fetch("/get-cart-items") // Endpoint ที่ส่งข้อมูลตะกร้าสินค้า
        .then((response) => response.json())
        .then((data) => {
          const cartContainer = document.querySelector(".cart__container");
          cartContainer.innerHTML = "";
  
          data.forEach((item) => {
            const itemElement = document.createElement("article");
            itemElement.classList.add("cart__card");
            itemElement.innerHTML = `
              <div class="cart__box">
                <img src="/path/to/image/${item.product.picture}" alt="" class="cart__img" />
              </div>
              <div class="cart__details">
                <h3 class="cart__title">${item.product.name}</h3>
                <span class="cart__price">$${item.product.price}</span>
                <div class="cart__amount">
                  <div class="cart__amount-content">
                    <!-- ควบคุมจำนวนสินค้าที่นี่ -->
                    <span class="cart__amount-box">
                      <i class="bx bx-minus"></i>
                    </span>
                    <span class="cart__amount-number">${item.quantity}</span>
                    <span class="cart__amount-box">
                      <i class="bx bx-plus"></i>
                    </span>
                  </div>
                  <i class="bx bx-trash-alt cart__amount-trash" data-product-id="${item.product.product_id}"></i>
                </div>
              </div>
            `;
            const dynamicCartContainer = document.querySelector(".dynamic-cart-container"); // เปลี่ยนชื่อตัวแปรเพื่อหลีกเลี่ยงความสับสน
            dynamicCartContainer.appendChild(itemElement);
          });
        })
        .catch((error) => console.error("Error:", error))
    }
  
  });
  