let homeview: Object = {
  state: {
    dialogFormVisible: false, //Display the modification box
    commentVisible: false, //Display the comment box
    uplistData: {}, //The content of the article to be modified
    Comment: {}, //Comment data
    loginVisible: false, //Display login failure box
    registerVisible: false, //Display registration failure box
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
    },
    CLOSE_DIA(state: any) {
      state.commentVisible = !state.commentVisible;
    },
  },
  actions: {},
};
export default homeview;
