{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d6cb0a44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Job_ID': [1, 2, 3, 4, 5], 'Role': ['Data Analyst', 'Data Scientist', 'Business Analyst', 'Data Engineer', 'ML Engineer'], 'Company': ['ABC Corp', 'XyZ Ltd', 'DataWorks', 'InfraTech', 'AI Labs'], 'Skills': ['Excel SQL Python', 'Python ML Statistics', 'Excel SQL PowerBI', 'Python SQL Spark', 'Python ML DeepLearning']}\n"
     ]
    }
   ],
   "source": [
    "job_data = {\n",
    "    \"Job_ID\": [1, 2, 3, 4, 5],\n",
    "    \"Role\": [\"Data Analyst\", \"Data Scientist\", \"Business Analyst\", \"Data Engineer\", \"ML Engineer\"],\n",
    "    \"Company\": [\"ABC Corp\", \"XyZ Ltd\", \"DataWorks\", \"InfraTech\", \"AI Labs\"],\n",
    "    \"Skills\": [\n",
    "        \"Excel SQL Python\",\n",
    "        \"Python ML Statistics\",\n",
    "        \"Excel SQL PowerBI\",\n",
    "        \"Python SQL Spark\",\n",
    "        \"Python ML DeepLearning\"\n",
    "    ]\n",
    "}\n",
    "print(job_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2136934d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Job Listings:\n",
      "\n",
      "ID: 1 | Role: Data Analyst | Company: ABC Corp | Skills: Excel SQL Python\n",
      "ID: 2 | Role: Data Scientist | Company: XYZ Ltd | Skills: Python ML Statistics\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 13\u001b[39m\n\u001b[32m      9\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m job \u001b[38;5;28;01min\u001b[39;00m job_data:\n\u001b[32m     10\u001b[39m     print(f\"ID: {job[\u001b[33m'id'\u001b[39m]} | Role: {job[\u001b[33m'role'\u001b[39m]} | Company: {job[\u001b[33m'company'\u001b[39m]} | Skills: {\u001b[33m' '\u001b[39m.join(job[\u001b[33m'skills'\u001b[39m])}\")\n\u001b[32m     11\u001b[39m \n\u001b[32m     12\u001b[39m \u001b[38;5;66;03m# 2) Add new job postings\u001b[39;00m\n\u001b[32m---> \u001b[39m\u001b[32m13\u001b[39m num = int(input(\u001b[33m\"\\nHow many job postings do you want to add? \"\u001b[39m))\n\u001b[32m     14\u001b[39m \n\u001b[32m     15\u001b[39m \u001b[38;5;66;03m# Find max existing ID\u001b[39;00m\n\u001b[32m     16\u001b[39m max_id = max(job[\u001b[33m\"id\"\u001b[39m] \u001b[38;5;28;01mfor\u001b[39;00m job \u001b[38;5;28;01min\u001b[39;00m job_data)\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: ''"
     ]
    }
   ],
   "source": [
    "# Initial job data\n",
    "job_data = [\n",
    "    {\"id\": 1, \"role\": \"Data Analyst\", \"company\": \"ABC Corp\", \"skills\": [\"Excel\", \"SQL\", \"Python\"]},\n",
    "    {\"id\": 2, \"role\": \"Data Scientist\", \"company\": \"XYZ Ltd\", \"skills\": [\"Python\", \"ML\", \"Statistics\"]}\n",
    "]\n",
    "\n",
    "# 1) Print job postings\n",
    "print(\"Job Listings:\\n\")\n",
    "for job in job_data:\n",
    "    print(f\"ID: {job['id']} | Role: {job['role']} | Company: {job['company']} | Skills: {' '.join(job['skills'])}\")\n",
    "\n",
    "# 2) Add new job postings\n",
    "while True:\n",
    "    num_input = input(\"\\nHow many job postings do you want to add? \").strip()\n",
    "    if num_input == \"\":\n",
    "        print(\"Please enter a number (or 0 to skip).\")\n",
    "        continue\n",
    "    try:\n",
    "        num = int(num_input)\n",
    "        break\n",
    "    except ValueError:\n",
    "        print(\"Invalid input. Enter a valid integer.\")\n",
    "\n",
    "# Find max existing ID\n",
    "max_id = max(job[\"id\"] for job in job_data)\n",
    "\n",
    "def new_func():\n",
    "    role = input(\"Enter role: \")\n",
    "    return role\n",
    "\n",
    "for i in range(num):\n",
    "    print(f\"\\nEntering details for job {i+1}:\")\n",
    "    role = new_func()\n",
    "    company = input(\"Enter company: \")\n",
    "    skills_input = input(\"Enter skills (comma or space separated): \")\n",
    "    \n",
    "    # Convert skills string into list\n",
    "    if \",\" in skills_input:\n",
    "        skills = [s.strip() for s in skills_input.split(\",\")]\n",
    "    else:\n",
    "        skills = skills_input.split()\n",
    "    \n",
    "    max_id += 1  # auto-increment ID\n",
    "    \n",
    "    new_job = {\n",
    "        \"id\": max_id,\n",
    "        \"role\": role,\n",
    "        \"company\": company,\n",
    "        \"skills\": skills\n",
    "    }\n",
    "    \n",
    "    job_data.append(new_job)\n",
    "\n",
    "# Final output\n",
    "print(\"\\nUpdated Job Listings:\\n\")\n",
    "for job in job_data:\n",
    "    print(f\"ID: {job['id']} | Role: {job['role']} | Company: {job['company']} | Skills: {' '.join(job['skills'])}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "934d242d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
