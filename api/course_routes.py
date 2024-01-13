
from flask import Blueprint, jsonify
import os

import xlrd

from .courses_data import courses


course_api = Blueprint('course_api', __name__)

@course_api.route('/getCourses', methods=['GET'])
def get_courses():

    return jsonify(courses)

@course_api.route('/schedules/<int:userid>/<int:planid>/<sheet_name>', methods=['GET'])
def get_schedule(userid, planid, sheet_name):
    file_name = "2024-SPRG Info.xls"
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, f"PlannerX_service/Users/{userid}/{planid}/2024-SPRG Info.xls")
    schedule = parse_xls(file_path, sheet_name)
    return jsonify(schedule)

def parse_xls(file_path, sheet_name):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_name(sheet_name)
    data = []
    for row_idx in range(1, sheet.nrows):  
        row_data = {}
        for col_idx in range(sheet.ncols):
            cell = sheet.cell(row_idx, col_idx)
            row_data[sheet.cell(0, col_idx).value] = cell.value
        data.append(row_data)
    return data


@course_api.route('/schedules/<int:userid>/<int:planid>/sheet_count', methods=['GET'])
def get_sheet_count(userid, planid):
    file_name = "2024-SPRG Info.xls"
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, f"PlannerX_service/Users/{userid}/{planid}/2024-SPRG Info.xls")
    workbook = xlrd.open_workbook(file_path)
    sheet_count = len(workbook.sheet_names())
    return jsonify({"total_sheets": sheet_count})


if __name__ == "__main__":
    semester = "2024-SPRG"  # Fall:"FALL", Summer:"SUMM", Spring:"SPRG"
    print(get_schedule(1,1,"Plan 1"))
    # getAndSaveSections("https://www.bu.edu/phpbin/course-search/section/?t=casaa103&amp;semester=2021-SUMM&amp;return=%2Fphpbin%2Fcourse-search%2Fsearch.php%3Fpage%3D0%26pagesize%3D100%26adv%3D1%26nolog%3D%26search_adv_all%3D%26yearsem_adv%3D2021-SUMM%26credits%3D%2A%26hub_match%3Dall%26pagesize%3D100", "CAS AA 103", "2021-SUMM")
