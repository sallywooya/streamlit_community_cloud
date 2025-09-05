#!/usr/bin/env python3
"""
Streamlit Components Demonstration Tool
Perfect for classroom teaching and student demonstrations

Run with: streamlit run codes_streamlit_components.py
"""

import streamlit as st
import time
import pandas as pd
import numpy as np
from datetime import datetime, date

# Page configuration - must be first Streamlit command
st.set_page_config(
    page_title="Streamlit Components Demo",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

def demo_basic_setup():
    """Basic page setup and text components"""
    st.header("🎯 Basic Setup & Text Components")
    
    st.markdown("""
    ### Text Display Methods
    Different ways to display text and information in Streamlit.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Text Functions")
        st.title("Title (st.title)")
        st.header("Header (st.header)")
        st.subheader("Subheader (st.subheader)")
        st.text("Plain text (st.text)")
        st.markdown("**Markdown** with *emphasis* (st.markdown)")
        st.write("Versatile write function (st.write)")
    
    with col2:
        st.subheader("📦 Status Messages")
        st.success("✅ Success message")
        st.info("ℹ️ Information message")
        st.warning("⚠️ Warning message")  
        st.error("❌ Error message")
        
        st.subheader("💻 Code Display")
        st.code("""
# Example code
import streamlit as st
st.write("Hello World!")
        """, language="python")

def demo_session_state():
    """Session state management"""
    st.header("💾 Session State Management")
    
    st.markdown("""
    ### Persistent Data Storage
    Session state allows data to persist between user interactions.
    """)
    
    # Initialize session state
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    if "user_data" not in st.session_state:
        st.session_state.user_data = {"name": "", "email": ""}
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔢 Counter Example")
        st.write(f"Current count: **{st.session_state.counter}**")
        
        button_col1, button_col2, button_col3 = st.columns(3)
        with button_col1:
            if st.button("➕ Add 1"):
                st.session_state.counter += 1
        with button_col2:
            if st.button("➖ Subtract 1"):
                st.session_state.counter -= 1
        with button_col3:
            if st.button("🔄 Reset"):
                st.session_state.counter = 0
    
    with col2:
        st.subheader("📝 User Data Example")
        name = st.text_input("Name:", value=st.session_state.user_data["name"])
        email = st.text_input("Email:", value=st.session_state.user_data["email"])
        
        if st.button("💾 Save Data"):
            st.session_state.user_data = {"name": name, "email": email}
            st.success("Data saved to session state!")
        
        st.write("**Stored data:**", st.session_state.user_data)

def demo_input_widgets():
    """Input widgets demonstration"""
    st.header("📝 Input Widgets")
    
    st.markdown("""
    ### User Input Components
    Various ways to collect user input in Streamlit applications.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔤 Text Inputs")
        name = st.text_input("Your name:", placeholder="Enter name...")
        password = st.text_input("Password:", type="password")
        message = st.text_area("Message:", placeholder="Type your message here...")
        
        st.subheader("🔢 Number Inputs")
        age = st.number_input("Age:", min_value=0, max_value=120, value=25)
        score = st.slider("Score:", 0, 100, 75)
        rating = st.select_slider("Rating:", options=['Poor', 'Fair', 'Good', 'Excellent'])
    
    with col2:
        st.subheader("🎯 Selection Widgets")
        option = st.selectbox("Choose option:", ["Option A", "Option B", "Option C"])
        multi_options = st.multiselect("Multiple choice:", ["Red", "Green", "Blue", "Yellow"])
        
        agree = st.checkbox("I agree to terms")
        choice = st.radio("Choose one:", ["Yes", "No", "Maybe"])
        
        st.subheader("📅 Date & Time")
        selected_date = st.date_input("Select date:")
        selected_time = st.time_input("Select time:")
        
        st.subheader("🎨 Special Inputs")
        color = st.color_picker("Pick color:", "#FF0000")
        
    # Display results
    if name:
        st.success(f"Hello **{name}**! You selected **{option}** and rated **{rating}**")

def demo_layout_components():
    """Layout and organization components"""
    st.header("📐 Layout & Organization")
    
    st.markdown("""
    ### Structuring Your App
    Components to organize content in columns, tabs, and containers.
    """)
    
    # Columns demonstration
    st.subheader("📊 Columns Layout")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Sales", "1,234", "12%")
    with col2:
        st.metric("Revenue", "$56.7K", "-2%")
    with col3:
        st.metric("Users", "891", "5%")
    with col4:
        st.metric("Growth", "23.4%", "1.2%")
    
    # Tabs demonstration
    st.subheader("📑 Tabs Layout")
    tab1, tab2, tab3 = st.tabs(["📈 Charts", "📊 Data", "⚙️ Settings"])
    
    with tab1:
        # Sample chart data
        chart_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            'Sales': [20, 45, 30, 55, 40],
            'Expenses': [15, 30, 25, 35, 28]
        })
        st.bar_chart(chart_data.set_index('Month'))
    
    with tab2:
        # Sample data table
        df = pd.DataFrame({
            'Product': ['A', 'B', 'C', 'D'],
            'Price': [10.99, 15.50, 8.75, 12.00],
            'Stock': [45, 23, 67, 12]
        })
        st.dataframe(df, use_container_width=True)
    
    with tab3:
        st.write("Configure your settings here:")
        st.toggle("Enable notifications")
        st.slider("Refresh rate (seconds):", 1, 60, 5)
    
    # Containers and expanders
    st.subheader("📦 Containers & Expanders")
    
    with st.container():
        st.write("This content is inside a container")
        
        with st.expander("🔍 Click to expand"):
            st.write("Hidden content that can be expanded!")
            st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

def demo_sidebar():
    """Sidebar demonstration"""
    st.header("🔧 Sidebar Usage")
    
    st.markdown("""
    ### Navigation & Controls
    The sidebar is perfect for app navigation, settings, and controls.
    """)
    
    # Sidebar content
    with st.sidebar:
        st.markdown("---")
        st.subheader("🎛️ Demo Controls")
        
        # Settings
        theme = st.selectbox("App Theme:", ["Light", "Dark", "Auto"])
        notifications = st.toggle("Enable Notifications", True)
        
        st.subheader("📊 Data Filters")
        date_range = st.date_input(
            "Date range:",
            value=(date.today(), date.today()),
            key="sidebar_date"
        )
        
        categories = st.multiselect(
            "Categories:",
            ["Technology", "Science", "Sports", "Music"],
            default=["Technology"]
        )
        
        st.subheader("🎯 Quick Actions")
        if st.button("📥 Export Data", key="sidebar_export"):
            st.success("Data exported!")
        
        if st.button("🔄 Refresh", key="sidebar_refresh"):
            st.success("Data refreshed!")
    
    # Main content showing sidebar values
    st.info(f"Current theme: **{theme}**")
    st.info(f"Notifications: **{'On' if notifications else 'Off'}**")
    st.info(f"Selected categories: **{', '.join(categories)}**")
    
    # Show some data based on sidebar selections
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Sample Chart")
        sample_data = pd.DataFrame({
            'Category': categories,
            'Value': np.random.randint(10, 100, len(categories))
        })
        if len(categories) > 0:
            st.bar_chart(sample_data.set_index('Category'))
    
    with col2:
        st.subheader("📋 Sample Data")
        st.write(sample_data if len(categories) > 0 else "No categories selected")

def demo_file_upload():
    """File upload demonstration"""
    st.header("📁 File Upload & Processing")
    
    st.markdown("""
    ### File Handling
    Upload and process different file types in your Streamlit app.
    """)
    
    uploaded_file = st.file_uploader(
        "Choose a file:",
        type=['txt', 'csv', 'json', 'pdf', 'jpg', 'png'],
        help="Upload any supported file type"
    )
    
    if uploaded_file is not None:
        # File information
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("File Size", f"{uploaded_file.size / 1024:.1f} KB")
        with col2:
            st.metric("File Type", uploaded_file.type)
        with col3:
            st.metric("File Name", uploaded_file.name)
        
        st.success(f"✅ Successfully uploaded: **{uploaded_file.name}**")
        
        # Handle different file types
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode()
            st.subheader("📄 Text File Content")
            st.text_area("File content:", content, height=200)
            
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            st.subheader("📊 CSV File Preview")
            st.dataframe(df.head(10))
            st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
            
        elif uploaded_file.type.startswith('image/'):
            st.subheader("🖼️ Image Preview")
            st.image(uploaded_file, caption=uploaded_file.name, width=400)
            
        else:
            st.write(f"**File uploaded:** {uploaded_file.name}")
            st.write("Preview not available for this file type.")
    
    else:
        st.info("👆 Please upload a file to see the processing demo")

def demo_interactive_widgets():
    """Interactive widgets demonstration"""
    st.header("🎮 Interactive Widgets")
    
    st.markdown("""
    ### Dynamic Components  
    Advanced interactive elements for engaging user experiences.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Progress & Status")
        
        if st.button("🚀 Start Process"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(101):
                progress_bar.progress(i)
                status_text.text(f'Processing... {i}%')
                time.sleep(0.02)
            
            st.success('✅ Process completed!')
        
        st.subheader("🎨 Color & Style")
        color = st.color_picker("Choose theme color:", "#FF6B6B")
        
        # Display color sample
        st.markdown(f"""
        <div style="
            width: 100%; 
            height: 60px; 
            background: linear-gradient(90deg, {color} 0%, {color}88 100%);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        ">
            Selected Color: {color}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📅 Date & Time Controls")
        
        selected_date = st.date_input("Event date:")
        selected_time = st.time_input("Event time:")
        
        st.write(f"**Scheduled for:** {selected_date} at {selected_time}")
        
        st.subheader("🎛️ Advanced Controls")
        
        # Range slider
        price_range = st.slider(
            "Price range:",
            0, 1000, (200, 800),
            format="$%d"
        )
        st.write(f"Price range: ${price_range[0]} - ${price_range[1]}")
        
        # Toggle switches
        features = {}
        features['notifications'] = st.toggle("Push notifications")
        features['auto_save'] = st.toggle("Auto-save", True)
        features['dark_mode'] = st.toggle("Dark mode")
        
        enabled_features = [k for k, v in features.items() if v]
        if enabled_features:
            st.success(f"Enabled: {', '.join(enabled_features)}")

def demo_data_display():
    """Data display and visualization"""
    st.header("📊 Data Display & Visualization")
    
    st.markdown("""
    ### Charts, Tables & Metrics
    Powerful ways to display data and create visualizations.
    """)
    
    # Generate sample data
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=30)
    df = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(100, 500, 30),
        'Expenses': np.random.randint(50, 200, 30),
        'Profit': np.random.randint(20, 150, 30)
    })
    df['Cumulative'] = df['Profit'].cumsum()
    
    # Metrics row
    st.subheader("📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Sales", f"${df['Sales'].sum():,}", f"{df['Sales'].iloc[-1] - df['Sales'].iloc[-2]:+d}")
    with col2:
        st.metric("Avg Profit", f"${df['Profit'].mean():.0f}", f"{df['Profit'].std():.1f}")
    with col3:
        st.metric("Best Day", f"${df['Sales'].max():,}", "🎯")
    with col4:
        st.metric("Growth Rate", "12.5%", "2.1%")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Daily Sales")
        st.line_chart(df.set_index('Date')[['Sales', 'Expenses']])
        
    with col2:
        st.subheader("💰 Profit Trend") 
        st.area_chart(df.set_index('Date')['Cumulative'])
    
    # Data table
    st.subheader("📋 Raw Data")
    
    # Add filters
    col1, col2 = st.columns(2)
    with col1:
        min_sales = st.slider("Minimum sales:", int(df['Sales'].min()), int(df['Sales'].max()), int(df['Sales'].min()))
    with col2:
        show_all = st.checkbox("Show all columns", True)
    
    filtered_df = df[df['Sales'] >= min_sales]
    
    if show_all:
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.dataframe(filtered_df[['Date', 'Sales', 'Profit']], use_container_width=True)
    
    st.info(f"Showing {len(filtered_df)} of {len(df)} records")

def demo_advanced_features():
    """Advanced Streamlit features"""
    st.header("🚀 Advanced Features")
    
    st.markdown("""
    ### Professional App Elements
    Advanced components for building production-ready applications.
    """)
    
    # Custom CSS styling
    st.markdown("""
    <style>
    .custom-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .highlight-box {
        background-color: #f0f2f6;
        border-left: 4px solid #FF6B6B;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Custom styled content
    st.markdown("""
    <div class="custom-card">
        <h3>🎨 Custom Styled Component</h3>
        <p>This demonstrates custom CSS styling within Streamlit apps!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📱 Mobile-Responsive Layout")
        
        # Responsive metrics
        metrics_data = [
            ("👥", "Users", "1,234", "+12%"),
            ("💰", "Revenue", "$45.6K", "+8%"),
            ("📈", "Growth", "23.4%", "+2.1%")
        ]
        
        for icon, label, value, delta in metrics_data:
            st.markdown(f"""
            <div class="highlight-box">
                <h4>{icon} {label}</h4>
                <h2>{value} <small style="color: green;">{delta}</small></h2>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🎯 Interactive Elements")
        
        # Multi-step form
        step = st.selectbox("Form Step:", ["Step 1: Basic Info", "Step 2: Preferences", "Step 3: Review"])
        
        if step == "Step 1: Basic Info":
            name = st.text_input("Full Name:")
            email = st.text_input("Email:")
            
        elif step == "Step 2: Preferences":
            interests = st.multiselect("Interests:", ["Tech", "Science", "Art", "Sports"])
            notifications = st.radio("Notifications:", ["Email", "SMS", "None"])
            
        else:  # Step 3
            st.success("✅ Ready to submit!")
            if st.button("🚀 Complete Registration"):
                st.balloons()
                st.success("Registration completed!")
    
    # Status indicators
    st.subheader("🔔 Status & Alerts")
    
    status_col1, status_col2, status_col3 = st.columns(3)
    
    with status_col1:
        if st.button("✅ Success Action"):
            st.success("Action completed successfully!")
    
    with status_col2:
        if st.button("⚠️ Warning Action"):
            st.warning("Please review your settings!")
    
    with status_col3:
        if st.button("❌ Error Action"):
            st.error("Something went wrong!")

def demo_mini_application():
    """Complete mini application example"""
    st.header("🏆 Complete Mini Application")
    
    st.markdown("""
    ### Task Management System
    A fully functional mini-app combining multiple Streamlit components.
    """)
    
    # Initialize session state
    if "tasks" not in st.session_state:
        st.session_state.tasks = [
            {"id": 1, "title": "Complete Streamlit tutorial", "status": "In Progress", "priority": "High", "due": "2024-02-15"},
            {"id": 2, "title": "Build demo application", "status": "Completed", "priority": "Medium", "due": "2024-02-10"},
        ]
        st.session_state.task_counter = 3
    
    # Sidebar for adding tasks
    with st.sidebar:
        st.subheader("➕ Add New Task")
        
        with st.form("add_task_form"):
            title = st.text_input("Task Title:")
            priority = st.selectbox("Priority:", ["High", "Medium", "Low"])
            due_date = st.date_input("Due Date:")
            
            if st.form_submit_button("Add Task"):
                if title:
                    new_task = {
                        "id": st.session_state.task_counter,
                        "title": title,
                        "status": "Todo",
                        "priority": priority,
                        "due": due_date.strftime("%Y-%m-%d")
                    }
                    st.session_state.tasks.append(new_task)
                    st.session_state.task_counter += 1
                    st.success(f"Added task: {title}")
                    st.rerun()
        
        st.divider()
        
        # Filters
        st.subheader("🔍 Filters")
        status_filter = st.selectbox("Status:", ["All", "Todo", "In Progress", "Completed"])
        priority_filter = st.selectbox("Priority:", ["All", "High", "Medium", "Low"])
    
    # Main task display
    tasks = st.session_state.tasks
    
    # Apply filters
    if status_filter != "All":
        tasks = [t for t in tasks if t["status"] == status_filter]
    if priority_filter != "All":
        tasks = [t for t in tasks if t["priority"] == priority_filter]
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    all_tasks = st.session_state.tasks
    with col1:
        st.metric("Total Tasks", len(all_tasks))
    with col2:
        completed = len([t for t in all_tasks if t["status"] == "Completed"])
        st.metric("Completed", completed)
    with col3:
        in_progress = len([t for t in all_tasks if t["status"] == "In Progress"])
        st.metric("In Progress", in_progress)
    with col4:
        high_priority = len([t for t in all_tasks if t["priority"] == "High"])
        st.metric("High Priority", high_priority)
    
    # Task list
    st.subheader(f"📋 Tasks ({len(tasks)} shown)")
    
    for task in tasks:
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
            
            with col1:
                if task["status"] == "Completed":
                    st.markdown(f"~~{task['title']}~~")
                else:
                    st.write(f"**{task['title']}**")
            
            with col2:
                priority_colors = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
                st.write(f"{priority_colors[task['priority']]} {task['priority']}")
            
            with col3:
                status_colors = {"Todo": "⚪", "In Progress": "🔵", "Completed": "✅"}
                st.write(f"{status_colors[task['status']]} {task['status']}")
            
            with col4:
                st.write(task['due'])
            
            with col5:
                if st.button("🗑️", key=f"delete_{task['id']}"):
                    st.session_state.tasks = [t for t in st.session_state.tasks if t['id'] != task['id']]
                    st.rerun()
            
            st.divider()
    
    if not tasks:
        st.info("No tasks match the current filters.")
    
    # Progress visualization
    if all_tasks:
        st.subheader("📊 Progress Overview")
        status_counts = {}
        for status in ["Todo", "In Progress", "Completed"]:
            status_counts[status] = len([t for t in all_tasks if t["status"] == status])
        
        progress_df = pd.DataFrame(list(status_counts.items()), columns=['Status', 'Count'])
        st.bar_chart(progress_df.set_index('Status'))

# Main application
def main():
    # Header
    st.title("🎯 Streamlit Components Demonstration")
    st.markdown("""
    ### Interactive Teaching Tool
    Select different components from the sidebar to demonstrate Streamlit capabilities to your students.
    """)
    
    # Sidebar navigation
    with st.sidebar:
        st.header("📚 Component Demos")
        
        demo_options = {
            "🎯 Basic Setup": demo_basic_setup,
            "💾 Session State": demo_session_state,
            "📝 Input Widgets": demo_input_widgets,
            "📐 Layout & Organization": demo_layout_components,
            "🔧 Sidebar Usage": demo_sidebar,
            "📁 File Upload": demo_file_upload,
            "🎮 Interactive Widgets": demo_interactive_widgets,
            "📊 Data & Visualization": demo_data_display,
            "🚀 Advanced Features": demo_advanced_features,
            "🏆 Mini Application": demo_mini_application
        }
        
        selected_demo = st.selectbox(
            "Choose demonstration:",
            list(demo_options.keys()),
            index=0
        )
        
        st.markdown("---")
        st.markdown("""
        **🎓 Teaching Tips:**
        - Select different components to show live examples
        - Students can interact with all elements
        - Perfect for classroom demonstrations
        - Each demo is self-contained and functional
        """)
        
        st.markdown("---")
        st.info("💡 **Tip:** Run with `streamlit run streamlit_components_demo.py`")
    
    # Show selected demonstration
    demo_options[selected_demo]()

if __name__ == "__main__":
    main()
