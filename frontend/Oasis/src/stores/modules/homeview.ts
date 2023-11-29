let homeview: Object = {
  state: {
    dialogFormVisible: false,
    commentVisible: false,
    uplistData: {},
    Comment: {},
    loginVisible: false,
    registerVisible: false,
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
    OPEN_DIA(state: any, paylog: any) {
      state.commentVisible = !state.commentVisible;
      state.Comment = paylog;
      console.log(state.Comment);
    },
    CLOSE_DIA(state: any) {
      state.commentVisible = !state.commentVisible;
    },
  },
  actions: {},
};
export default homeview;
