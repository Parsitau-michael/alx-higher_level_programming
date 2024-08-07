$("#add_item").on("click", () => {
  const newItem = $("<li>Item</li>");
  $("UL.my_list").append(newItem);
});
