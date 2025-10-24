type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let currentNum = init;
    function increment(){
        return ++currentNum ;
    }
    function decrement(){
        
        return --currentNum;
    }
    function reset(){
        return (currentNum = init);
    }
    return {increment, decrement, reset}
}
/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */