// Define an array to store the available laptops with their configurations and prices.
const prompt = require("prompt-sync")({ sigint: true });
const laptops = [
  { id: 1, name: 'Laptop A', ram: 8, storage: 256, price: 28000 },
  { id: 2, name: 'Laptop B', ram: 16, storage: 512, price: 61200 },
  { id: 3, name: 'Laptop C', ram: 32, storage: 1000, price: 120000 },
];

// Initialize an empty shopping cart.
const cart = [];

// Function to add a laptop to the cart with dynamic pricing.
function addToCart(laptopId, RAMSize, storageSize) {
  const laptop = laptops.find((l) => l.id === laptopId);

  if (!laptop) {
    console.log('Laptop not found.');
    return;
  }

  // Debugging output
  console.log(`Initial laptop price: $${laptop.price}`);
  console.log(`RAMSize: ${RAMSize}`);
  console.log(`StorageSize: ${storageSize}`);

  // Define a base price for the laptop.
  let basePrice = laptop.price;

  // Calculate the price based on RAM and storage.
  // Adding $10 for each additional GB of RAM,
  // and $0.5 for each additional GB of storage.
  basePrice += (RAMSize - laptop.ram) * 10;
  basePrice += (storageSize - laptop.storage) * 0.5;

  // Debugging output
  console.log(`Final laptop price: $${basePrice}`);

  cart.push({
    name: laptop.name,
    ram: RAMSize,
    storage: storageSize,
    price: basePrice,
  });

  console.log(`Added to the cart. Price: $${basePrice}`);
}
// Function to remove an item from the cart based on its index.
function removeFromCart(index) {
    if (index >= 0 && index < cart.length) {
      const removedItem = cart.splice(index, 1);
      console.log(`Removed from the cart.`);
    } else {
      console.log('Invalid index. Item not removed.');
    }
  }

// Function to calculate the total price of items in the cart.
function calculateTotal() {
  let total = 0;
  for (const item of cart) {
    total += item.price;
  }
  return total;
  console.log(`Price: $${basePrice}`);
}

// Main program loop
while (true) {
  console.log('\nOptions:');
  console.log('1. Add a laptop to the cart');
  console.log('2. Remove an item from the cart');
  console.log('3. Calculate the total price');
  console.log('4. Exit');
  const choice = parseInt(prompt('Enter your choice:'));

  switch (choice) {
    case 1:
      const laptopId = parseInt(prompt('Enter laptop ID:'));
      const RAMSize = parseInt(prompt('Enter RAM size (GB):'));
      const storageSize = parseInt(prompt('Enter storage size (GB):'));
      addToCart(laptopId, RAMSize, storageSize);
      break;

    case 2:
      const index = parseInt(prompt('Enter the index of the item to remove:'));
      removeFromCart(index);
      break;

    case 3:
      const total = calculateTotal();
      console.log(`Total Price: $${total}`);
      break;

    case 4:
      console.log('Exiting the program.');
      return;

    default:
      console.log('Invalid choice. Please try again.');
  }
}
