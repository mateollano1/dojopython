from datetime import datetime, timedelta

from flask import render_template

from app import global_data
from . import dashboard
from .. import plot

current_date = datetime.now()
init_date = (current_date.replace(day=1) - timedelta(days=180)).replace(day=1)

@dashboard.route('/home')
def homepage():
    total_df = global_data.get_total_df()
    last_load_date = datetime.now()

    account_ids_list = total_df.account_id.unique()

    time_line_json = plot.plot_time_lime(account_ids_list[0], total_df, last_load_date)

    return render_template('dashboard/index.html', title="Dojo Python Panda",
                           time_line_json=time_line_json,
                           account_ids_list=account_ids_list,
                           active_page='dashboard',
                           current_date=datetime.strftime(last_load_date, '%d/%m/%Y'))

@dashboard.route('/time_line/<int:account_id>')
def get_time_line_plot(account_id):
    total_df = global_data.get_total_df()
    last_load_date = datetime.now()
    time_line_json = plot.plot_time_lime(account_id, total_df, last_load_date)
    return time_line_json
