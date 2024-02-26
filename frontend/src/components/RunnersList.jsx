import React from "react";

const RunnersList = ({ runners }) => {
  return (
    <div>
      <h3>Runners List 2024</h3>
      <table id="runners">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Category</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {runners.map((runner) => (
            <tr key={runner.id}>
              <td>
                {runner.first_name} {runner.last_name}
              </td>
              <td>{runner.email}</td>
              <td>{runner.category}</td>
              <td>
                <button>Edit</button>
                <button>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RunnersList;
