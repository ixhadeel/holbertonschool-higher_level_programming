document.addEventListener('DOMContentLoaded', function () {
  const list = document.querySelector('#my_list, .my_list');
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');

  addItem.addEventListener('click', function () {
    const item = document.createElement('li');
    item.textContent = 'Item';
    list.appendChild(item);
  });

  removeItem.addEventListener('click', function () {
    if (list.lastElementChild) {
      list.lastElementChild.remove();
    }
  });

  clearList.addEventListener('click', function () {
    list.innerHTML = '';
  });
});
