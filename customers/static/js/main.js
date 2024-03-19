const pizzaTypesUrl = "/customers/getpizzatypes/";
const cheeseUrl = "/customers/getcheeses/";
const toppingsUrl = "/customers/gettoppings/";

const fetchDataPizzaBase = async (url, elementId) => {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  const select = document.getElementById(elementId);
  data.forEach((item) => {
    let option = document.createElement("option");
    option.value = item.pizzaTypeName;
    option.textContent = item.pizzaTypeName;
    select.append(option);
  });
};

const fetchDataCheeseType = async (url, elementId) => {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  const select = document.getElementById(elementId);
  data.forEach((item) => {
    let option = document.createElement("option");
    option.value = item.cheeseName;
    option.textContent = item.cheeseName;
    select.append(option);
  });
};

document.addEventListener("DOMContentLoaded", () => {
  fetchDataPizzaBase("/customers/getpizzatypes/", "pizzaBase1");
  fetchDataCheeseType("/customers/getcheeses/", "cheeseType1");

  fetchDataPizzaBase("/customers/getpizzatypes/", "pizzaBase2");
  fetchDataCheeseType("/customers/getcheeses/", "cheeseType2");

  fetchDataPizzaBase("/customers/getpizzatypes/", "pizzaBase3");
  fetchDataCheeseType("/customers/getcheeses/", "cheeseType3");

  document
    .getElementById("orderForm1")
    .addEventListener("submit", async (e) => {
      e.preventDefault();

      // Collecting the form data
      const pizzaBase = document.getElementById("pizzaBase1").value;
      const cheeseType = document.getElementById("cheeseType1").value;
      const selectedOptions = document.querySelectorAll(
        'input[name="option"]:checked'
      );
      if (selectedOptions.length < 5) {
        alert("Please select at least 5 options.");
        event.preventDefault();
      }
      // Add your code to submit the form data to the server
    });

  document
    .getElementById("orderForm2")
    .addEventListener("submit", async (e) => {
      e.preventDefault();

      // Collecting the form data
      const pizzaBase = document.getElementById("pizzaBase2").value;
      const cheeseType = document.getElementById("cheeseType2").value;
      const selectedToppings = Array.from(
        document.getElementById("toppings2").selectedOptions
      ).map((option) => option.value);
      const numberOfPizzas = document.getElementById("number2").value;

      if (selectedToppings.length < 5) {
        alert("Please select 5 toppings minimum");
        return;
      }

      // Add your code to submit the form data to the server
    });

  document
    .getElementById("orderForm3")
    .addEventListener("submit", async (e) => {
      e.preventDefault();

      // Collecting the form data
      const pizzaBase = document.getElementById("pizzaBase3").value;
      const cheeseType = document.getElementById("cheeseType3").value;
      const selectedToppings = Array.from(
        document.getElementById("toppings3").selectedOptions
      ).map((option) => option.value);
      const numberOfPizzas = document.getElementById("number3").value;

      if (selectedToppings.length < 5) {
        alert("Please select 5 toppings minimum");
        return;
      }

      // Add your code to submit the form data to the server
    });
});

//     const orderData = {
//       pizzaBase,
//       cheeseType,
//       toppings: selectedToppings,
//       quantity: numberOfPizzas,
//     };

//     // Post the collected data as JSON to the server
//     try {
//       const response = await fetch("/api/submit_order/", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify(orderData),
//       });

//       if (response.ok) {
//         // Assuming the server returns a JSON object
//         const result = await response.json();
//         console.log(result);
//         alert("Order placed successfully!");
//       } else {
//         console.error("Failed to submit order.", response.statusText);
//         alert("There was a problem with your order. Please try again.");
//       }
//     } catch (error) {
//       console.error("Error:", error);
//       alert("An error occurred while submitting your order. Please try again.");
//     }
//   });
// });
