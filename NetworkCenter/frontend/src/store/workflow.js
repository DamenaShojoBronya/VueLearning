// src/store/workflow.js
export default {
    namespaced: true,
    state: {
      selectedWorkflow: null,
    },
    mutations: {
      setSelectedWorkflow(state, workflow) {
        state.selectedWorkflow = workflow;
      },
    },
  };
  