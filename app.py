import streamlit as st

# Initialize session state
if "booked_seats" not in st.session_state:
    st.session_state.booked_seats = []
if "seat_index" not in st.session_state:
    st.session_state.seat_index = 0
if "name" not in st.session_state:
    st.session_state.name = ""

MAX_SEATS = 10
TICKET_TYPES = {
    "Movie": 150,
    "Train": 100,
    "Concert": 300
}

# Title
st.title("🎫 SmartTicket Booking System")

# Get user's name
if st.session_state.name == "":
    st.session_state.name = st.text_input("Enter your name")

# Booking form
if st.session_state.name:
    with st.form("ticket_booking_form"):
        ticket_type = st.selectbox("Choose Ticket Type", list(TICKET_TYPES.keys()))
        quantity = st.number_input("Enter number of tickets", min_value=1, max_value=MAX_SEATS - st.session_state.seat_index)
        submit = st.form_submit_button("Book Ticket")

        if submit:
            if st.session_state.seat_index + quantity > MAX_SEATS:
                st.error("Not enough seats available.")
            else:
                for i in range(quantity):
                    seat = f"{ticket_type} Seat {st.session_state.seat_index + 1}"
                    st.session_state.booked_seats.append(seat)
                    st.session_state.seat_index += 1
                total = TICKET_TYPES[ticket_type] * quantity
                st.success(f"Booked {quantity} {ticket_type} ticket(s). Total: Rs.{total}")

# Booking summary
if st.session_state.seat_index > 0:
    st.markdown("### ✅ Booking Summary")
    st.write(f"**Customer:** {st.session_state.name}")
    for seat in st.session_state.booked_seats:
        st.write(f"• {seat}")
else:
    if st.session_state.name:
        st.info("No tickets booked yet.")

st.markdown("---")
st.caption("Thank you for using SmartTicket!")
