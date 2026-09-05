import os

# Wallet Transactions
wt_mig = "database/migrations/2026_09_02_215449_create_wallet_transactions_table.php"
with open(wt_mig, "r") as f:
    content = f.read()

new_wt = """            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->string('type'); // topup, semester_registration, course_registration
            $table->decimal('amount', 12, 2);
            $table->string('description')->nullable();
            $table->string('reference_id')->nullable(); // Can be payment_id, semester_reg_id, etc.
            $table->timestamps();"""
content = content.replace("            $table->id();\n            $table->timestamps();", new_wt)
with open(wt_mig, "w") as f:
    f.write(content)

# Semester Registrations
sr_mig = "database/migrations/2026_09_02_215450_create_semester_registrations_table.php"
with open(sr_mig, "r") as f:
    content = f.read()

new_sr = """            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->foreignId('academic_session_id')->constrained()->cascadeOnDelete();
            $table->decimal('amount', 12, 2);
            $table->string('status')->default('paid');
            $table->timestamps();"""
content = content.replace("            $table->id();\n            $table->timestamps();", new_sr)
with open(sr_mig, "w") as f:
    f.write(content)


# Course Registrations
cr_mig = "database/migrations/2026_09_02_215451_create_course_registrations_table.php"
with open(cr_mig, "r") as f:
    content = f.read()

new_cr = """            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->foreignId('academic_session_id')->constrained()->cascadeOnDelete();
            $table->foreignId('course_id')->constrained()->cascadeOnDelete();
            $table->decimal('amount', 12, 2);
            $table->string('status')->default('paid');
            $table->timestamps();"""
content = content.replace("            $table->id();\n            $table->timestamps();", new_cr)
with open(cr_mig, "w") as f:
    f.write(content)

# Add Wallet Balance
ab_mig = "database/migrations/2026_09_02_215452_add_wallet_balance_to_users_table.php"
with open(ab_mig, "r") as f:
    content = f.read()

new_up = """    public function up(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->decimal('wallet_balance', 12, 2)->default(0)->after('email');
        });
    }"""
new_down = """    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn('wallet_balance');
        });
    }"""
content = content.replace("""    public function up(): void
    {
        Schema::table('users', function (Blueprint $table) {
            //
        });
    }""", new_up)
content = content.replace("""    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            //
        });
    }""", new_down)
with open(ab_mig, "w") as f:
    f.write(content)

print("Migrations updated successfully.")
