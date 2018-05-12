
function chunkArrayInGroups(arr, size) {
  // Break it up.
  var arrNew = [];
  for (var i = 0; i < arr.length; i += size){
      arrNew.push(arr.slice(i, i + size));
    }
  //arr.push;
  return arrNew;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);