let homeview: Object = {
  state: {
    dialogFormVisible: false,
    uplistData: {},
  },
  getters: {},
  mutations: {
    SET_DIALOG(state: any, paylog: any) {
      state.dialogFormVisible = !state.dialogFormVisible;

      state.uplistData = paylog;
    },
    DIALOG(state: any) {
      state.dialogFormVisible = !state.dialogFormVisible;
    },
  },
  actions: {},
};
export default homeview;
