import fs from 'fs';
import { courseDetails } from './resources/js/data/courseDetails.js';

fs.writeFileSync('parsed_courses.json', JSON.stringify(courseDetails, null, 2));
