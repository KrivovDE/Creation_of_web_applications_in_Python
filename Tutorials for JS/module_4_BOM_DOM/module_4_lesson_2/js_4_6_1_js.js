// Для каждого узла дерева список его дочерних элементов
// можно получить через коллекцию childNodes:
// let v = document.body.childNodes
// console.log(typeof (v))

// for (let i = 0; i < document.body.childNodes.length; i++) {
//     console.log( document.body.childNodes[i] );
// }
///////////////////////////////////////////////////////////////
// for (let child of document.body.childNodes) {
//     console.log( child );
// }
///////////////////////////////////////////////////////////////
// let vel = document.documentElement;
// let first = vel.firstChild;
// let last = vel.lastChild;
//
// console.log( first );
// console.log( last );
// console.log( vel );
///////////////////////////////////////////////////////////////
console.log(document.head.nextSibling);
console.log(document.body.previousSibling)
console.log(document.body.parentNode);
///////////////////////////////////////////////////////////////




///////////////////////////////////////////////////////////////
