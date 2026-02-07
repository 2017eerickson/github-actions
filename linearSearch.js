/*
DATA: 
  an arr or string
LOGIC:
  search through iterable in order one by one
  stopping at the first instances index
INPUT:
  search term and iterable
OUTPUT:
  index of the first instance
*/

function linearSearch(searchTerm, arr) {
  for( let i = 0; i < arr.length; i++){
    if (arr[i] == searchTerm){
      return i;
    }
  }
  return undefined;
}
let nums = [1,3,4,4]
// console.log(linearSearch("a","caop"))

function globalLinearSearch(searchTerm, arr) {
  let allIndex = [] ;
  for( let i = 0; i < arr.length; i++){
    if(arr[i] == searchTerm){
      allIndex.push(i);
      }
    } 
  return allIndex
}
console.log(globalLinearSearch(1, [1, 2, 3]
  
))

module.exports = { linearSearch, globalLinearSearch };
