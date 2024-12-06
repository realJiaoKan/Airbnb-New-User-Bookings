import pandas as pd
import streamlit as st

# 定义数据加载路径
path_to_data = "result_analysis.csv"  # 替换为您的数据文件路径


# 初始化 session_state
def init_session_state():
    if "loaded" not in st.session_state:
        # 加载数据
        result_analysis = pd.read_csv(path_to_data)

        # 提取需要展示的列
        columns_to_show = [
            "id",
            "date_account_created_year",
            "timestamp_first_active_yearmonth",
            "gender",
            "age",
            "language",
            "train_top5_rank_decoded",
            "train_actual_decoded",
            "ndcg_score",
        ]
        result_analysis = result_analysis[columns_to_show]

        # 存储到 session_state
        st.session_state.loaded = True
        st.session_state.result_analysis = result_analysis


# 展示目的地信息
def display_destination_info(index):
    data = st.session_state.result_analysis.iloc[index]
    st.subheader("Selected User Information")

    # 左右两列显示基础信息
    col1, col2 = st.columns(2)
    with col1:
        st.info("ID")
        st.success(data["id"])
        st.info("Year Account Created")
        st.success(data["date_account_created_year"])
        st.info("Year-Month First Active")
        st.success(data["timestamp_first_active_yearmonth"])
    with col2:
        st.info("Gender")
        st.success(data["gender"])
        st.info("Age")
        st.success(data["age"])
        st.info("Language")
        st.success(data["language"])

    st.subheader("Destination Prediction and Metrics")

    # 显示预测前五目的地和真实值
    col_pred, col_actual = st.columns(2)
    with col_pred:
        st.info("Top 5 Predicted Destinations")
        st.success(", ".join(eval(data["train_top5_rank_decoded"])))  # 转换为列表显示
    with col_actual:
        st.info("Actual Destination")
        st.success(data["train_actual_decoded"])

    # 显示 NDCG 分数
    st.info("NDCG Score")
    st.success(round(data["ndcg_score"], 4))


# 主应用
def app():
    init_session_state()
    st.title("Destination Prediction Viewer")

    # 用户选择一个索引查看详情
    options = ["-"] + list(range(len(st.session_state.result_analysis)))
    index = st.selectbox(label="Choose a user index", options=options, index=0)

    if index != "-":
        display_destination_info(int(index))


if __name__ == "__main__":
    app()
