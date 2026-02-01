/**
 * Problem 1: Transform Orders with Aggregation
 * 
 * Aggregate orders by date, sum the amounts, and sort by total revenue descending.
 * 
 * @param {Array<{date: string, amount: number}>} orders - Array of order objects
 * @returns {Array<{date: string, total: number}>} - Sorted array of aggregated orders
 * 
 * Example:
 * Input: [{ date: "2025-10-28", amount: 100 }, { date: "2025-10-28", amount: 50 }, { date: "2025-10-29", amount: 200 }]
 * Output: [{ date: "2025-10-29", total: 200 }, { date: "2025-10-28", total: 150 }]
 */

const testCases = [
    {
      id: 1,
      input: [
        { date: "2025-10-28", amount: 100 },
        { date: "2025-10-28", amount: 50 },
        { date: "2025-10-29", amount: 200 }
      ]
    },
    {
      id: 2,
      input: [
        { date: "2025-10-25", amount: 100 },
        { date: "2025-10-26", amount: 200 },
        { date: "2025-10-25", amount: 150 },
        { date: "2025-10-27", amount: 50 }
      ]
    },
    {
      id: 3,
      input: [
        { date: "2025-10-28", amount: 75.50 },
        { date: "2025-10-28", amount: 24.50 },
        { date: "2025-10-29", amount: 100.00 }
      ]
    },
    {
      id: 4,
      input: [
        { date: "2025-10-28", amount: 500 }
      ]
    }
  ];
  
function transformOrders(orders) {
    // TODO: Implement your solution here
    let map = new Map()
    orders.reduce((acc, curr)=>{
        console.log(acc,"acc", curr);
        
    })
  }
  


  console.log(transformOrders(testCases));
  