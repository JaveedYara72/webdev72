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

const fetchDataToppings = async (url, elementId) => {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  const select = document.getElementById(elementId);
  data.forEach((item) => {
    let option = document.createElement("option");
    option.value = item.toppingName;
    option.textContent = item.toppingName;
    select.append(option);
  });
};

document.addEventListener("DOMContentLoaded", () => {
  fetchDataPizzaBase("/customers/getpizzatypes/", "pizzaBase");
  fetchDataCheeseType("/customers/getcheeses/", "cheeseType");
  fetchDataToppings("/customers/gettoppings/", "toppings");

  document.getElementById("orderForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    // Collecting the form data
    const pizzaBase = document.getElementById("pizzaBase").value;
    const cheeseType = document.getElementById("cheeseType").value;
    const selectedToppings = Array.from(
      document.getElementById("toppings").selectedOptions
    ).map((option) => option.value);
    const numberOfPizzas = document.getElementById("number").value;

    if (selectedToppings.length < 5) {
      alert("Please select 5 toppings minium");
      return;
    }
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
